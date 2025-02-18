import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
