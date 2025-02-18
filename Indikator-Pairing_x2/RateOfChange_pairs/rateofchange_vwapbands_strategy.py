import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und VWAPBands
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'VWAPBands': 1.0
        })
    )
