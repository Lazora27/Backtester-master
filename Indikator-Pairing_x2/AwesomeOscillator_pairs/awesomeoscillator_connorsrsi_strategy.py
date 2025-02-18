import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'ConnorsRSI': 1.0
        })
    )
