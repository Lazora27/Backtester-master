import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'IchimokuCloud': 1.0
        })
    )
