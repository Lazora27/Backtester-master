import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
