import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und DemandIndex
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'DemandIndex': 1.0
        })
    )
