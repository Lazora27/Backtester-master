import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und VWAPBands
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'VWAPBands': 1.0
        })
    )
