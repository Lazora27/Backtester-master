import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_ExtensionProjections_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und ExtensionProjections
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'ExtensionProjections': {
                'class': ExtensionProjections,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExtensionProjections'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'ExtensionProjections': 1.0
        })
    )
