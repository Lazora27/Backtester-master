import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'ProjectionBands': 1.0
        })
    )
