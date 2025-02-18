import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersDecycler_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersDecycler und TimeCycle
    """
    
    params = (
        ('indicators', {
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'EhlersDecycler': 1.0,
            'TimeCycle': 1.0
        })
    )
