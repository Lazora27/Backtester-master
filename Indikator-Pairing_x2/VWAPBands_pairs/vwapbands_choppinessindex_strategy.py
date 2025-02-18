import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_ChoppinessIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und ChoppinessIndex
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'ChoppinessIndex': 1.0
        })
    )
