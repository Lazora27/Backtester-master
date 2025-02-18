import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
