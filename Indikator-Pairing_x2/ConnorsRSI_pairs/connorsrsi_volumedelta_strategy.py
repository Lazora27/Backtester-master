import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'VolumeDelta': 1.0
        })
    )
