import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und MassIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'MassIndex': 1.0
        })
    )
