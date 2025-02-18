import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
