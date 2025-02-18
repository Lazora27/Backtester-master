import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und BarStrength
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'BarStrength': 1.0
        })
    )
