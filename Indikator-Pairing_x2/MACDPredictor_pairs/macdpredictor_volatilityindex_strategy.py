import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'VolatilityIndex': 1.0
        })
    )
