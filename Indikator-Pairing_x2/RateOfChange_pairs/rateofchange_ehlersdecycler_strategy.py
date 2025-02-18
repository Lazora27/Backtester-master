import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'EhlersDecycler': 1.0
        })
    )
