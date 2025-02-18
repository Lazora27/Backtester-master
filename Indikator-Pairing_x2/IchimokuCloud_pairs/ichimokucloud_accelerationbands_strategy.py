import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'AccelerationBands': 1.0
        })
    )
