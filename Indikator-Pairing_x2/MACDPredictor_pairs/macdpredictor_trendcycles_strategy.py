import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'TrendCycles': 1.0
        })
    )
