import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und VWAPBands
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'VWAPBands': 1.0
        })
    )
