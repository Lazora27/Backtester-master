import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'ConnorsRSI': 1.0
        })
    )
