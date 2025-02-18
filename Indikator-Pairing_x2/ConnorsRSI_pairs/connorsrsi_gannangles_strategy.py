import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und GannAngles
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'GannAngles': 1.0
        })
    )
