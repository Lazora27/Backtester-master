import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KDJIndicator_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KDJIndicator und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'KDJIndicator': {
                'class': KDJIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KDJIndicator'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'KDJIndicator': 1.0,
            'MACDPredictor': 1.0
        })
    )
