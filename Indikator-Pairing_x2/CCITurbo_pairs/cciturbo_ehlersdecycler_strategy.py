import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CCITurbo_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CCITurbo und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'CCITurbo': 1.0,
            'EhlersDecycler': 1.0
        })
    )
