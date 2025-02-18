import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'ParabolicSAR': 1.0
        })
    )
