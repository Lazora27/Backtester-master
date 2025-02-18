import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_CenterOfGravity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und CenterOfGravity
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'CenterOfGravity': {
                'class': CenterOfGravity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CenterOfGravity'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'CenterOfGravity': 1.0
        })
    )
