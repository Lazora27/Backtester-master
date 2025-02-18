import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'ParabolicSAR': 1.0
        })
    )
