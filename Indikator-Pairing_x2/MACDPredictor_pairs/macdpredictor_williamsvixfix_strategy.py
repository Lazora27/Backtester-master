import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_WilliamsVIXFix_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und WilliamsVIXFix
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'WilliamsVIXFix': {
                'class': WilliamsVIXFix,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsVIXFix'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'WilliamsVIXFix': 1.0
        })
    )
