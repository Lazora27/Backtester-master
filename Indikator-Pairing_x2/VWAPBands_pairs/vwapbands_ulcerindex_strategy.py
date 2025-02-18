import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_UlcerIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und UlcerIndex
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'UlcerIndex': {
                'class': UlcerIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndex'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'UlcerIndex': 1.0
        })
    )
