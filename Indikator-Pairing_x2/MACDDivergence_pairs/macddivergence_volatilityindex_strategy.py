import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_VolatilityIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und VolatilityIndex
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'VolatilityIndex': 1.0
        })
    )
