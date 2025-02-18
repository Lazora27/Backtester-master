import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MassIndex_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MassIndex und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MassIndex': 1.0,
            'EhlersDecycler': 1.0
        })
    )
