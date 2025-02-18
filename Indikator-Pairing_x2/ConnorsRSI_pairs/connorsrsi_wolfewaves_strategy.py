import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'WolfeWaves': 1.0
        })
    )
