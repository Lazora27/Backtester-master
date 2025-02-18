import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_AdvancedCandlePattern_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und AdvancedCandlePattern
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'AdvancedCandlePattern': 1.0
        })
    )
