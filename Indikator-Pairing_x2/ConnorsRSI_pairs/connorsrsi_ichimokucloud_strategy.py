import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_IchimokuCloud_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und IchimokuCloud
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'IchimokuCloud': 1.0
        })
    )
