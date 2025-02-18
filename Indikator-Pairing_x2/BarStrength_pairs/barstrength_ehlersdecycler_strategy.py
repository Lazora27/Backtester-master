import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BarStrength_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BarStrength und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'BarStrength': 1.0,
            'EhlersDecycler': 1.0
        })
    )
