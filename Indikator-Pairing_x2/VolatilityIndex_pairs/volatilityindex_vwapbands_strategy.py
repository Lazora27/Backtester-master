import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und VWAPBands
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'VWAPBands': 1.0
        })
    )
