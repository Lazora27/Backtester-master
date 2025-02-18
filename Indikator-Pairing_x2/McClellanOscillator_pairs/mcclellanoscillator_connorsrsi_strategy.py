import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ConnorsRSI': 1.0
        })
    )
