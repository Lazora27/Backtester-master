import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und VWAPBands
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'VWAPBands': 1.0
        })
    )
