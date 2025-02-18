import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'EhlersDecycler': 1.0
        })
    )
