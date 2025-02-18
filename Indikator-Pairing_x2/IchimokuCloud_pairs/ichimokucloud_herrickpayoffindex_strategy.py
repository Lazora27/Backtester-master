import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
