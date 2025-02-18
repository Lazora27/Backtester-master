import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvancedCandlePattern_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvancedCandlePattern und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'AdvancedCandlePattern': {
                'class': AdvancedCandlePattern,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvancedCandlePattern'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'AdvancedCandlePattern': 1.0,
            'EhlersDecycler': 1.0
        })
    )
