import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ConnorsRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ConnorsRSI
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ConnorsRSI': 1.0
        })
    )
