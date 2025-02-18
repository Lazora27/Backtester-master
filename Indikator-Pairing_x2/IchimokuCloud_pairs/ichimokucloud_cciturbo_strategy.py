import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und CCITurbo
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'CCITurbo': 1.0
        })
    )
