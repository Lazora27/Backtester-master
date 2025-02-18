import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und GannFans
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'GannFans': 1.0
        })
    )
