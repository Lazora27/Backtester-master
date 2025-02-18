import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_LiquidityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und LiquidityIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'LiquidityIndex': {
                'class': LiquidityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_LiquidityIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'LiquidityIndex': 1.0
        })
    )
