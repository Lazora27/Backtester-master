import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'AverageTrueRange': 1.0
        })
    )
