import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und DemandIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'DemandIndex': 1.0
        })
    )
