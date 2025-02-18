import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'IchimokuCloud': 1.0
        })
    )
