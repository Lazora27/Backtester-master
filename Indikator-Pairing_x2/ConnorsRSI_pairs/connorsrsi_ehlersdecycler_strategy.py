import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'EhlersDecycler': 1.0
        })
    )
