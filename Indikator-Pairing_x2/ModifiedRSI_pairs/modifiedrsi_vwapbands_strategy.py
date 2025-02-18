import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und VWAPBands
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'VWAPBands': 1.0
        })
    )
