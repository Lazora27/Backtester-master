import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
