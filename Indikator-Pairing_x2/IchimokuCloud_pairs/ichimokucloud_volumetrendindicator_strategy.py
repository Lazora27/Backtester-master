import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
