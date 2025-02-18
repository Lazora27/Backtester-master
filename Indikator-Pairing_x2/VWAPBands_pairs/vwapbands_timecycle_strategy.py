import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und TimeCycle
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'TimeCycle': 1.0
        })
    )
