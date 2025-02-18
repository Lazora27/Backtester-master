import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'EhlersDecycler': 1.0
        })
    )
